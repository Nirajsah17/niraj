# Compiler and flags
CXX = g++                         # Use g++ as the compiler
CXXFLAGS = -Wall -std=c++17       # Enable all warnings, use C++17 standard

# Output target
TARGET = app

# Object files
OBJS = main.o math.o

# Rule to build final executable
$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

# Compile main.cpp into main.o (only if main.cpp or math.h changed)
main.o: main.cpp math.h
	$(CXX) $(CXXFLAGS) -c main.cpp

# Compile math.cpp into math.o (only if math.cpp or math.h changed)
math.o: math.cpp math.h
	$(CXX) $(CXXFLAGS) -c math.cpp

# Clean command to remove .o files and the binary
clean:
	rm -f *.o $(TARGET)
