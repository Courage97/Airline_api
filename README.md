## Backend Review

The backend is built with Django and serves as the core API layer powering the Airline Passenger Satisfaction Prediction app. It loads the trained XGBoost model and expected feature columns to ensure consistent and accurate predictions.

Key functionalities include:

- **Input Validation:** Uses Django REST Framework serializers to validate incoming passenger data against the model’s required features.
- **Prediction Endpoint:** Receives passenger data, preprocesses it with one-hot encoding aligned to the training phase, and returns satisfaction predictions along with confidence scores.
- **Prediction Logging:** Saves each prediction and related metadata (e.g., seat number, flight details) in the database for auditing and future analysis.
- **History Endpoint:** Provides access to recent prediction logs to support transparency and monitoring.

This backend setup fully aligns with the project goals by operationalizing the trained machine learning model into a scalable and maintainable AI-powered service. It enables real-time passenger satisfaction predictions, which can improve airline service responsiveness and customer experience.
