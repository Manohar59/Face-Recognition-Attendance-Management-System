import traceback
try:
    import face_recognition_models
    print("Successfully imported face_recognition_models")
    print("Location:", face_recognition_models.__file__)
except Exception:
    traceback.print_exc()
