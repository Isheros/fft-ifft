cd frontend
docker build -t front:v2 .
cd ..

cd app
docker build -t back:v2 .
cd ..

docker-compose up

# docker run -d --name fftPy --network fft -p 5000:5000 back:v2


# docker run -itd --name fftFront --network fft \
# -e REACT_APP_API_URL=http://fftPy \
# -e REACT_APP_API_PORT=5000 -p 3000:3000 front:v2

# docker stop fftfront
# docker rm fftfront
# docker image rm front:v2
# cd frontend
# docker build -t front:v2 .
# cd ..
# docker-compose up


# docker stop fftback
# docker rm fftback
# docker image rm back:v2
# cd app
# docker build -t back:v2 .
# cd ..
# docker-compose up


# docker run --rm -it --network fft-ifft_fftNet archlinux

# cd frontend
# docker build -t front:v2 .
# cd ..

# cd app
# docker build -t back:v2 .
# cd ..
# docker-compose up
