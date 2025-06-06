FROM debian:bookworm

ENV TZ=Asia/Yangon

RUN apt-get update -y && apt-get install wget -y

RUN wget https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && dpkg -i packages-microsoft-prod.deb && rm packages-microsoft-prod.deb

RUN apt-get update -y && apt-get install -y aspnetcore-runtime-9.0 && apt-get clean -y
