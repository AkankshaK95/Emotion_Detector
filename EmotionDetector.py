import datetime
import cv2
from deepface import DeepFace
import time
import random

cap = cv2.VideoCapture(0) # replace 0 with your video file path
# cap = cv2.VideoCapture("InputStreams/[m3u8.dev]2023_07_17 13_14_50.mp4")
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50) # position of the subtitles on the screen
fontScale = 1
color = (255, 255, 255) # color of the subtitles in BGR format
thickness = 2 # thickness of the subtitles

# Working segment...
if __name__ == '__main__':
    #cap = cv2.VideoCapture('Eloclips/Recording122.mp4')
    # cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot access webcam")

    start_time = None
    duration = 12
    buffer_frames = []  
    event_duration = 3
    # fps = int(cap.get(cv2.CAP_PROP_FPS))
    fps=10
    buffer_size = fps*duration

    clip_buffer = []
    clip_name_prefix = 'clip_'
    clip_file_format = '.mp4'
    clips_folder = 'GeneratedClips2/'

    global clipcnt
    clipcnt=random.randint(20,10000)

    print("FPS: ", fps)

    while True:
        ret, frame = cap.read()
        frame1 = frame.copy()
        
        if not ret:
            break
        
        # detect face and extract face embeddings
        detected_faces = DeepFace.extract_faces(frame, detector_backend='opencv', enforce_detection=False)
        #(frame, detector_backend='opencv', enforce_detection=False)
        if len(detected_faces) == 0:
            continue # skip frame if no face is detected
        elif len(detected_faces) > 1:
            # if multiple faces are detected, take the first one
            face = detected_faces[0]
        else:
            face = detected_faces[0]
            
            
        text = f"{len(detected_faces)} face(s) detected"
        cv2.putText(frame, text, org, font, fontScale, color, thickness, cv2.LINE_AA)
        
        #print(face.keys())
        #print(face['face'])
        #print(face['facial_area'])
        #print(face['confidence'])
        
        if face != None:
            x, y, w, h = face['facial_area']['x'], face['facial_area']['y'], face['facial_area']['w'], face['facial_area']['h']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            face_img = frame[y:(y + h), x:(x + w)]
            
            # Get emotions scores
            emotions = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
            
            #buffer_frames.append(emotions)
            
            if len(buffer_frames)==0:
                buffer_frames.append(emotions)
                clip_buffer.append(frame1)
                
            if len(buffer_frames) < buffer_size:
                buffer_frames.append(emotions)
                clip_buffer.append(frame1)
            
            # If buffer is full, remove oldest frame
            if len(buffer_frames) > buffer_size:
                buffer_frames.pop(0)
                clip_buffer.pop(0)
                
            # Check if happy emotion has been present for more than event_duration seconds
            if len(buffer_frames) == buffer_size: 
                happy_count, surprise_count, disgust_count, fear_count, angry_count, sad_count = 0, 0, 0, 0, 0, 0
                for i in range(len(buffer_frames)):
                    #print('Debug')
                    if buffer_frames[i][0]['emotion']['happy'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'happy':
                        happy_count += 1
                    elif buffer_frames[i][0]['emotion']['surprise'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'surprise':
                        surprise_count += 1
                    elif buffer_frames[i][0]['emotion']['disgust'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'disgust':
                        disgust_count += 1
                    elif buffer_frames[i][0]['emotion']['fear'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'fear':
                        fear_count += 1
                    elif buffer_frames[i][0]['emotion']['angry'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'angry':
                        angry_count += 1
                    elif buffer_frames[i][0]['emotion']['sad'] > 0.5 and buffer_frames[i][0]['dominant_emotion'] == 'sad':
                        sad_count += 1
                    else:    continue
                if happy_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str('_happy_')+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1
                
                elif surprise_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1
                
                elif disgust_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1
                
                elif fear_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1

                elif angry_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1

                elif sad_count >= (event_duration*fps): 
                    # Start recording clip
                    # Save clip to file
                    out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                    print(len(clip_buffer))
                    for clip in clip_buffer:
                        out.write(clip)
                    out.release()
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    for i in range(int(event_duration*fps)):
                        buffer_frames.pop(0)
                        clip_buffer.pop(0)
                    '''
                    clipcnt+=1
                
                
                # elif (surprise_count+happy_count+sad_count+fear_count+disgust_count+angry_count) >= (event_duration*fps): 
                #     # Start recording clip
                #     # Save clip to file
                #     out = cv2.VideoWriter(clips_folder+clip_name_prefix+str(clipcnt)+clip_file_format, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame.shape[1], frame.shape[0]))
                #     print(len(clip_buffer))
                #     for clip in clip_buffer:
                #         out.write(clip)
                #     out.release()
                #     for i in range(int(event_duration*fps)):
                #         buffer_frames.pop(0)
                #         clip_buffer.pop(0)
                #     '''
                #     for i in range(int(event_duration*fps)):
                #         buffer_frames.pop(0)
                #         clip_buffer.pop(0)
                #     '''
                #     clipcnt+=1
            
            # Get current timestamp
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Show the emotions scores and timestamp on the frame
            emotions_text = ""
            value = emotions[0]['emotion']
            #print(value)
            for key in value.keys():
                emotions_text+= f"{key}: {value[key]:.4f}"
                emotions_text+="\n"
            
            #print(emotions_text)
            #print("ts: ", datetime.datetime.now())
            #print("Dominant_emotion: ", emotions[0]['dominant_emotion'])
            
            # Split the text into lines
            lines = emotions_text.split('\n')
            
            y=300
            for line in lines:
                cv2.putText(frame, line, (100, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)
                y += 18
            
            # Show the emotions scores and timestamp on the frame
            #cv2.putText(frame, emotions_text, (50, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.34, (255, 255, 0), 1)
            cv2.putText(frame, "Timestamp: " + timestamp, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow('original frame',frame)
        
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27: # press q or Esc to exit
            break

    cap.release()
    cv2.destroyAllWindows()
