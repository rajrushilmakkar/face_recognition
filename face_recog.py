import face_recognition as fr
import cv2 as cv
#from PIL import Image
global face
global face_locations
global frame
img=fr.load_image_file("rushil_makkar.jpg")
img1=fr.load_image_file("samyak_jain.jpeg")
img_enc=fr.face_encodings(img)[0]
img1_enc=fr.face_encodings(img1)[0]
known_face_encodings=[
    img_enc,img1_enc
]
known_face_names=[
    "Rushil Makkar","Samyak Jain"
]
cap=cv.VideoCapture(0)
def face_identify():
    try:
        for (top,right,bottom,left),face_encoding in zip(face_locations,frame_encs):
            matches=fr.compare_faces(known_face_encodings,face_encoding)
            name="Unknown"
            if True in matches:
                match_index=matches.index(True)
                name=known_face_names[match_index]
            cv.putText(frame,name,(left,top),cv.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            cv.rectangle(frame,(left,top),(right,bottom),(255,255,0),2)
    except:
        pass
while(True):
    _,frame=cap.read()
    try:
        frame_encs=fr.face_encodings(frame,face_locations)
    except:
        pass
    face_locations=fr.face_locations(frame)
    
    #print(face_locations)
    face_identify()
    
        
    cv.imshow("Camera",frame)
    
    print(len(face_locations))
    key=cv.waitKey(1)
    if(key==27):break
    

cap.release()
cv.destroyAllWindows()
