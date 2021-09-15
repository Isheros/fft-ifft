cd front
docker build -t front:v2 .

cd app
docker build -t back:v2 .

docker run -d --name fftPy --network fft -p 5000:5000 back:v2


docker run -itd --name fftFront --network fft \
-e REACT_APP_API_URL=http://fftPy \
-e REACT_APP_API_PORT=5000 -p 3000:3000 front:v2

docker stop fftFront
docker rm fftFront


docker stop fftPy
docker rm fftPy