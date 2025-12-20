CONTAINER=fastapi
IMAGE=nixos-server-fastapi

if [[ -n $1 ]]; then
	CONTAINER=$1
fi	
if [[ -n $2 ]]; then
	IMAGE=$2
fi
echo $CONTAINER	
echo $IMAGE

docker stop $CONTAINER && docker rm $CONTAINER

docker rmi $IMAGE
