from rest_framework import serializers
from .models import Bill, Mess, Hostel
from authentication.models import UserProfile


class HostelListSerializer(serializers.ModelSerializer):
    """
    Serializer for hostel list view.
    """
    class Meta:
        model = Hostel
        fields = ('id', 'name',)


class MessDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for mess list and detail view.
    """
    class Meta:
        model = Mess
        fields = ('id', 'name', 'menu',)


class MessBillSerializer(serializers.Serializer):
    """
    Serializer for showing the billing of individual students.
    """

    def validate(self, data):
        """
        Checks if the current user is subscribed to the mess
        with given id. Raises error if not subscribed.
        """
        mess_id = self.context['mess_id']
        user = self.context['request'].user
        user_profile = UserProfile.objects.filter(user=user).first()

        if user_profile.mess_id != mess_id:
            raise serializers.ValidationError(
                'You are not subscribed to this mess')

        data['user_profile'] = user_profile
        return data

    def get_bill_details(self):
        """
        Fetches the billing details of the current user
        and returns the serialized bill details.
        """
        data = self.validated_data
        user_profile = data.get('user_profile')
        mess = Mess.objects.filter(id=user_profile.mess_id).first()

        bill = Bill.objects.filter(
            user_profile=user_profile, mess=mess).first()
        serialized_bill = BillSerializer(bill)
        return serialized_bill.data


class BillSerializer(serializers.ModelSerializer):
    """
    Helper serializer for serializing the bill objects.
    """
    name = serializers.CharField(source='user_profile.name')
    mess = serializers.CharField(source='mess.name')

    class Meta:
        model = Bill
        fields = ('name', 'mess', 'monthly_bill', 'extra_charges',)


class MessCancelSerializer(serializers.Serializer):
    """
    Serializer for cancelling the mess subscription.
    """

    def validate(self, data):
        """
        Checks if the current user is subscribed to the mess
        with given id. Raises error if not subscribed.
        """
        mess_id = self.context['mess_id']
        user = self.context['request'].user
        user_profile = UserProfile.objects.filter(user=user).first()

        if user_profile.mess_id != mess_id:
            raise serializers.ValidationError(
                'You are not subscribed to this mess')

        data['user_profile'] = user_profile
        return data

    def cancel_mess(self):
        """
        Cancels the mess subscription of the current user by
        setting mess id to None and deleting the bill object
        for the current user and the current mess.
        """
        data = self.validated_data
        mess_id = self.context['mess_id']
        user_profile = data.get('user_profile')

        mess = Mess.objects.filter(id=mess_id).first()
        bill = Bill.objects.filter(
            user_profile=user_profile, mess=mess).first()
        bill.delete()
        user_profile.mess_id = None
        user_profile.save()
