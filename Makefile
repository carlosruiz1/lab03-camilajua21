
.PHONY: clean check check-ej2 check-ej3 check-ej4

check:
	gcc -g -o ll_equal.out ll_equal.c
	gcc -g -o ll_cycle.out ll_cycle.c
	gcc -g -o ll_lfsr.out ll_lfsr.c
	python check.py

check-ej2: 
	gcc -g -o ll_equal.out ll_equal.c
	python check.py 2

check-ej3: 
	gcc -g -o ll_cycle.out ll_cycle.c
	python check.py 3

check-ej4: 
	gcc -g -o ll_lfsr.out ll_lfsr.c
	python check.py 4

clean:
	$(RM) *.out
