import os.path
import cv2


def add_frames_to_video():
    video_path = r"D:\Datalyca\BirdieIns\singles-backview-docker-v1\preSingles\preprocessing\Pose_Estimation\data\video"
    video_file = "video12.mp4"
    video_split = video_file.split('.')
    out_video_path = os.path.join(video_path,
                                  f"{video_split[0]}_fr.{video_split[-1]}")
    _cap = cv2.VideoCapture(os.path.join(video_path, video_file))
    _fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    _fps = _cap.get(cv2.CAP_PROP_FPS)
    _total_frames = _cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"total frames : {_total_frames}")
    _dim = (
        int(_cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    _out = cv2.VideoWriter(out_video_path, _fourcc, _fps, _dim)
    ct_fr = 0
    while ct_fr < _total_frames:
        try:
            ret, frame = _cap.read()
            if ret:
                ct_fr += 1
                # Frame number in all frames
                frame_number = f'{ct_fr}'
                frame_number_size, _ = cv2.getTextSize(frame_number,
                                                       cv2.FONT_HERSHEY_PLAIN,
                                                       2,
                                                       1)
                cv2.rectangle(frame, (10, 20),
                              (10 + frame_number_size[0],
                               20 - frame_number_size[1]),
                              (0, 0, 0),
                              -1)
                cv2.putText(frame,
                            frame_number,
                            (10, 20), cv2.FONT_HERSHEY_PLAIN,
                            2,
                            (155, 255, 150), lineType=cv2.LINE_AA)

                _out.write(frame)
                _per_comp = (ct_fr / _total_frames) * 100
                if _per_comp > 95:
                    print(
                        f"{round(_per_comp, 2)} % completed")
                elif _per_comp % 10.0 == 0:
                    print(
                        f"{round(_per_comp)} % completed")
        except Exception:
            print(f"error {ct_fr}")
    _cap.release()
    _out.release()


if __name__ == '__main__':
    add_frames_to_video()
