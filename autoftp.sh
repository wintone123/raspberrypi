#!bin.bash
path="/media/pi/RaSegate/movie"
cd $path

# download all files to local
server=ftp.bitport.io   
username=ragnarok0521@hotmail.com
password=dnj0521
lftp <<EOF
open ftp://$username:$password@$server
ls
mirror 
exit
EOF