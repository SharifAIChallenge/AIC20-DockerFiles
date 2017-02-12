CXX = g++ --std=c++0x
JSONPATH = jsoncpp-src-0.5.0/include
FLAGS = -Wall -L/usr/local/lib -Wl,-rpath=/usr/local/lib -I$(JSONPATH)
LIBS = -lpthread

TARGET = flows.out

JSON_OBJECTS = jsoncpp-src-0.5.0/src/lib_json/json_reader.o \
	       jsoncpp-src-0.5.0/src/lib_json/json_value.o \
	       jsoncpp-src-0.5.0/src/lib_json/json_writer.o

BASE_SOURCES = $(wildcard */*.cpp) $(wildcard *.cpp)
BASE_OBJ = ${BASE_SOURCES:.cpp=.o}
BASE_OBJECTS = ${BASE_OBJ:.c=.o}

OBJECTS = ${BASE_OBJECTS} ${JSON_OBJECTS}

all: ${TARGET}

${TARGET}: ${OBJECTS}
	${CXX} ${FLAGS} -o ${TARGET} ${OBJECTS} ${LIBS}

clean:
	tmpfolder=`echo /tmp/CF-clean-$$$$.removed` && mkdir -p $$tmpfolder && touch a && mv -t $$tmpfolder/ a `for a in ${OBJECTS} ${TARGET} *~ base/*~ user/*~ ; do if [ -e $$a ]; then echo $$a; fi; done`

.cpp.o:
	${CXX} ${FLAGS} -c $< -o $@
.c.o:
	${CXX} ${FLAGS} -c $< -o $@

.PHONY: all clean submit
