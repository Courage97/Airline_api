from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import PredictionInputSerializer
from .models import predict_passenger_satisfaction, PredictionLog, model_columns


# === 1. Single Passenger Prediction ===
class SatisfactionPredictView(APIView):
    def post(self, request):
        serializer = PredictionInputSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            # Extract AI-only input
            model_input = {k: v for k, v in data.items() if k in model_columns}
            result = predict_passenger_satisfaction(model_input)

            # Save to database
            PredictionLog.objects.create(
                input_data=model_input,
                prediction=result["prediction"],
                confidence=result["confidence"],
                seat_number=data.get("seat_number"),
                location=data.get("location"),
                flight_date=data.get("flight_date"),
                flight_number=data.get("flight_number"),
                note_to_attendant=data.get("note_to_attendant"),
            )

            return Response({
                "prediction": result["prediction"],
                "confidence": result["confidence"],
                "message": f"A flight attendant will attend to you at seat {data.get('seat_number', 'N/A')} shortly."
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# === 2. View Recent Predictions (History) ===
@api_view(['GET'])
def prediction_history(request):
    logs = PredictionLog.objects.all().order_by('-timestamp')[:100]
    data = [
        {
            "prediction": log.prediction,
            "confidence": log.confidence,
            "timestamp": log.timestamp,
            "seat_number": log.seat_number,
            "location": log.location,
            "flight_date": log.flight_date,
            "flight_number": log.flight_number,
            "note_to_attendant": log.note_to_attendant,
            "input_data": log.input_data
        }
        for log in logs
    ]
    return Response(data)
