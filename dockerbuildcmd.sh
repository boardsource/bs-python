cd ports/raspberrypi
make BOARD=boardsource_blok
sleep 100
cp ports/raspberrypi/build-boardsource_blok/firmware.uf2 /build_out/boardsource_blok.uf2