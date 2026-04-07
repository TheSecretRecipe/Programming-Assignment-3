CXX = g++
CXXFLAGS = -std=c++17 -O2 -Wall -Wextra

all:
	$(CXX) $(CXXFLAGS) -o hvlcs src/main.cpp

clean:
	rm -f hvlcs
