# To be run on serve platform

docker build -t dregistry.moisesdiaz.ai:443/pneumonia-mlservice:1.1.1 -f pneumonia-mlservice.Dockerfile .

docker login -u druid -p b085y3QsIHhYmXiJ dregistry.moisesdiaz.ai:443

docker push dregistry.moisesdiaz.ai:443/pneumonia-mlservice:1.1.1