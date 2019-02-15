program main
  implicit none
  integer :: a(10), n, i
  n = 10
  print *, n
  do i = 1, n
    a(i) = i
  end do
  do i = 1, n
    print *, a(i)
  end do
end program main

