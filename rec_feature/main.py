import face_recognition
import numpy as np

def matcher():
    # Load a sample picture and learn how to recognize it.
    known_image = face_recognition.load_image_file("malan.jpg")
    encoding = face_recognition.face_encodings(known_image)


    # Load an image with unknown faces
    unknown_image = face_recognition.load_image_file("harvard.jpg")

    # Find all the faces and face encodings in the unknown image
    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encoding, face_encoding)

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(encoding, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:

            # Return True
            return True
    return False

print(matcher())