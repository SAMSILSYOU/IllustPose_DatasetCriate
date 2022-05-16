import cv2
from matplotlib.pyplot import text
import numpy as np
import glob
import math
from PIL import Image
import json
#コールバック関数
#マウスイベントが起こるとここへ来る

def read_image(): #座標打ち込み用関数

    data = []        # 画像データ用
    point = np.zeros((17,3,))
    point[:,2:3] = 2
    points = []
    win_name = 'put point'
    win_name2 = 'parts'
    fileA = '26'
    dataset = dict()
    
  

    R = [255,255,255,255,255,255,0,0,0,0,0,0,0,63,127,191,255]
    G = [255,0,63,127,191,255,255,255,255,255,255,0,0,0,0,0,0]
    B = [255,0,0,0,0,0,0,0,63,127,191,255,255,255,255,255,255]
    ptlist = ['nose','right shoulder', 'right elbow',
              'right hand','left shoulder','left elbow','left hand',
              'right hip','right knee','right foot','left hip',
              'left knee', 'left foot', 'right eye' ,'left eye',
              'right ear','left ear']


    def partsread(part,img2): #部位のテキスト更新用関数
        img2 = np.ones((100,300,3), np.uint8) * 255
        text = '{}'.format(part) + ':' +'{}'.format(ptlist[part])
        cv2.putText(img2, text , (16, 32), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 0), 2)
        cv2.imshow(win_name2,img2)
        

    

    def glob_files(path):


        def printCoor(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDOWN:
                print(x, y)
                parts = part
                cv2.circle(img, (x, y), 5, (R[part], G[part], B[part]), -1)
                point[parts][0] = math.floor(x/2)
                point[parts][1] = math.floor(y/2)
                point[parts][2] = 1
                print(point)
                print(num)
               

            else:
                return

            cv2.imshow(win_name,img)


        files = glob.glob(path + "/*.jpg")  # pathにある画像を読み込む
        

        # 各ファイルを処理
        count = 0
        num = 0
        for f in files:
            part = 0
            if num >= len(files): break
            num += 1
            #画像のウインドウに名前をつけ、コールバック関数をセット
            cv2.namedWindow(win_name)
            cv2.namedWindow(win_name2)
            cv2.setMouseCallback(win_name,printCoor)
            # 画像ファイルを読む
            img = Image.open(f)    # Pillow(PIL)で画像読込み。色順番はRGB
            img2 = np.ones((100,300,3), np.uint8) * 255
            img3 = Image.open(f)    # Pillow(PIL)で画像読込み。色順番はRGB
            cv2.moveWindow(win_name, 300, 200)
            img = np.asarray(img)  # ndarray化
            img3 = np.asarray(img)  # ndarray化
            img3 = cv2.resize(img, dsize=(368, 368))  # 画像サイズを220px × 220pxにする
            img = cv2.resize(img, dsize=(440, 440))  # 画像サイズを220px × 220pxにする
            
           
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img3 = cv2.cvtColor(img3, cv2.COLOR_RGB2BGR)

            partsread(part, img2)

            cv2.imshow(win_name,img)
            

            

            while True:
                key = cv2.waitKey(0)
                if key == 100: #'d'更新
                   part = part + 1 
                   if part >= 17:
                       part = 0
                   partsread(part, img2)
                
                if key == 97: #'a'更新
                   part = part - 1
                   if part < 0:
                       part = 16
                   partsread(part, img2)
                  
                if key == 114: #'r'リセット
                    point[part][0] = 0
                    point[part][1] = 0
                    point[part][2] = 2
                    print(point)
                  

                if key == 27:
                    for c in range (17):
                      if point[c][2] == 1:
                         count = count + 1
                    break
                        
            cv2.destroyAllWindows()

            
                    
            # 画像データ(img)とラベルデータ(label)をx, y のそれぞれのリストに保存
            file = 'dataset/{}'.format(fileA) + '/{}_'.format(fileA) + '{}.jpg'.format(num)
            cv2.imwrite(file, img3)
            print('Written to {}'.format(file))
            data.append(img3)
            points.append(point)
            #"{}".format(fileA) + "{}.jpg".format(num)
            dataset[num] = {                                    "dataset": "COCO_val",
                                                                "isValidation": 0.000,
                                                                "img_paths": "{}_".format(fileA) + "{}.jpg".format(num),
                                                                "img_width": 368.000,
                                                                "img_height": 368.000,
                                                                "objpos": [184.000,184.000],
                                                                "image_id": 36.000,
                                                                "bbox": [000.000,000.000,368.000,368.000],
                                                                "segment_area": 86145.297,
                                                                "num_keypoints": count,
                                                                  "jointself":[
                                                                  [point[0][0],point[0][1],point[0][2]],
                                                                  [point[1][0],point[1][1],point[1][2]],
                                                                  [point[2][0],point[2][1],point[2][2]],
                                                                  [point[3][0],point[3][1],point[3][2]],
                                                                  [point[4][0],point[4][1],point[4][2]],
                                                                  [point[5][0],point[5][1],point[5][2]],
                                                                  [point[6][0],point[6][1],point[6][2]],
                                                                  [point[7][0],point[7][1],point[7][2]],
                                                                  [point[8][0],point[8][1],point[8][2]],
                                                                  [point[9][0],point[9][1],point[9][2]],
                                                                  [point[10][0],point[10][1],point[10][2]],
                                                                  [point[11][0],point[11][1],point[11][2]],
                                                                  [point[12][0],point[12][1],point[12][2]],
                                                                  [point[13][0],point[13][1],point[13][2]],
                                                                  [point[14][0],point[14][1],point[14][2]],
                                                                  [point[15][0],point[15][1],point[15][2]],
                                                                  [point[16][0],point[16][1],point[16][2]],                                                               
                                                                   ],
                                                                "scale_provided": 1.000,
                                                                "joint_others": [],
                                                                "annolist_index": 1.000,
                                                                "people_index": 1.000,
                                                                "numOtherPeople": 0.000,
                                                                "scale_provided_other": {
                                                                    "_ArrayType_": "double",
                                                                    "_ArraySize_": [0,0],
                                                                    "_ArrayData_": None
                                                                },
                                                                "objpos_other": {
                                                                    "_ArrayType_": "double",
                                                                    "_ArraySize_": [0,0],
                                                                    "_ArrayData_": None
                                                                },
                                                                "bbox_other": {
                                                                    "_ArrayType_": "double",
                                                                    "_ArraySize_": [0,0],
                                                                    "_ArrayData_": None
                                                                },
                                                                "segment_area_other": {
                                                                    "_ArrayType_": "double",
                                                                    "_ArraySize_": [0,0],
                                                                    "_ArrayData_": None
                                                                },
                                                                "num_keypoints_other": {
                                                                    "_ArrayType_": "double",
                                                                    "_ArraySize_": [0,0],
                                                                    "_ArrayData_": None
                                                                }                                                          
                                                            }
            
           
                                                                     
            print(dataset)
        
            point[:] = np.zeros((17,3,))
            point[:,2:3] = 2
            count = 0
            



    
    glob_files("./data/")  # 各画像のフォルダーを読む
    print("file: " )

    with open('{}'.format(fileA) +'.json', 'w') as fp :
        json.dump(dataset, fp , ensure_ascii=False, indent=2, sort_keys=False, separators=(',', ': '))

if __name__ == '__main__':
    read_image()

