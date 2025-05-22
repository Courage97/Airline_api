from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    # === AI Model Features ===
    Gender = serializers.CharField()
    Customer_Type = serializers.CharField()
    Age = serializers.IntegerField()
    Type_of_Travel = serializers.CharField()
    Class = serializers.CharField()
    Flight_Distance = serializers.IntegerField()
    Seat_comfort = serializers.IntegerField()
    Departure_Arrival_time_convenient = serializers.IntegerField()
    Food_and_drink = serializers.IntegerField()
    Gate_location = serializers.IntegerField()
    Inflight_wifi_service = serializers.IntegerField()
    Inflight_entertainment = serializers.IntegerField()
    Online_support = serializers.IntegerField()
    Ease_of_Online_booking = serializers.IntegerField()
    On_board_service = serializers.IntegerField()
    Leg_room_service = serializers.IntegerField()
    Baggage_handling = serializers.IntegerField()
    Checkin_service = serializers.IntegerField()
    Cleanliness = serializers.IntegerField()
    Online_boarding = serializers.IntegerField()
    Departure_Delay_in_Minutes = serializers.IntegerField()
    Arrival_Delay_in_Minutes = serializers.IntegerField()

    # === Metadata (not used in prediction but logged) ===
    seat_number = serializers.CharField(required=False, allow_blank=True)
    location = serializers.CharField(required=False, allow_blank=True)
    flight_date = serializers.DateField(required=False)
    flight_number = serializers.CharField(required=False, allow_blank=True)
    note_to_attendant = serializers.CharField(required=False, allow_blank=True)
