CC = gcc
OBJS = test2.o 
TARGET = test_object

.SUFFIXES : .c .o

all : $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $(OBJS)


clean :
	rm -f $(OBJS) $(TARGET)

