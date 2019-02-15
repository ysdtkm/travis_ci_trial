TARGET = a.out
DEBUG = yes
STD = c++0x

CXX = g++
ifeq ($(DEBUG),yes)
  ifeq ($(STD),c++17)
    EXTRA = -fsanitize=bounds-strict
  else
    EXTRA =
  endif
  CXXFLAGS = -std=$(STD) -O0 -g3 -Wall -Wextra $(EXTRA)
else
  CXXFLAGS = -std=$(STD) -O2 -match=native
endif

exec: $(TARGET)
	./$<

$(TARGET): main.cc Makefile
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -rf *.o *.mod *.log $(TARGET) core.*

.PHONY: clean debug

