# tutorial
dataset : https://www.kaggle.com/datasets/ulrikthygepedersen/pokemon-stats  
python 3.11.4

docker build -t pokemon:first  
docker run -it -v "/data:/data" pokemon:first ./attack/  
defense도 똑같이  
final_calc는 -p 5000:5000 추가  
  
입력하는 칸 만드는 방법을 몰라서 한가지 포켓몬으로 고정 -> 추후 수정  
포켓몬 배틀에서 결정력과 내구력을 측정하여 출력
