TARGET = a.out
FC = mpif90
DEBUG = yes

ifeq ($(DEBUG),yes)
  FFLAGS := -std=f95 -Wall -Wuninitialized -O0 -g3 -fbounds-check \
            -fbacktrace -fdump-core -ffpe-trap=invalid,zero,overflow -fimplicit-none \
            -finit-real=snan -finit-integer=-858993460
else
  FFLAGS := -std=f95 -O2 -march=native -fbacktrace -fdump-core
endif

debug: $(TARGET)
	mpiexec --oversubscribe -n 4 ./$<

$(TARGET): main.f90 Makefile
	$(FC) $(FFLAGS) $< -o $@

clean:
	rm -rf *.o *.mod *.log $(TARGET) core.*

.PHONY: clean debug

