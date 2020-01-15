PROTOC_VERSION = 3.11.2
PROTOC = build/bin/protoc

all: build fk-atlas.proto.json fk-atlas.pb.go src/fk-atlas.pb.c src/fk-atlas.pb.h

node_modules/.bin/pbjs:
	npm install

fk-atlas.proto.json: node_modules/.bin/pbjs fk-atlas.proto
	pbjs fk-atlas.proto -t json -o fk-atlas.proto.json

src/fk-atlas.pb.c src/fk-atlas.pb.h: fk-atlas.proto
	$(PROTOC) --nanopb_out=./src fk-atlas.proto

fk-atlas.pb.go: fk-atlas.proto
	$(PROTOC) --go_out=./ fk-atlas.proto

clean:
	rm -rf build *.pb.go *.pb.c *.pb.h fk-atlas.proto.json

build: protoc-$(PROTOC_VERSION)-linux-x86_64.zip
	mkdir -p build
	cd build && unzip ../protoc-$(PROTOC_VERSION)-linux-x86_64.zip

protoc-$(PROTOC_VERSION)-linux-x86_64.zip:
	wget "https://github.com/protocolbuffers/protobuf/releases/download/v$(PROTOC_VERSION)/protoc-$(PROTOC_VERSION)-linux-x86_64.zip"

veryclean:
