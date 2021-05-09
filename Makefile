CC=g++
CFLAGS=-Wall
SOURCES=main.cc
LDFLAGS=`root-config --libs --cflags`
OBJECTS=$(SOURCES:.cc=.o)
EXECUTABLE=newFile

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(SOURCES) $(LDFLAGS) -o $@

.cc.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm ./*~ ./*.o
