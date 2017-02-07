	.global _start
_start:
	@load the character address
	ADR R1, string

	@print
	MOV R7, #4
	MOV R0, #1
	MOV R2, #14
	SWI 0


	@exit
	MOV R7, #1
	SWI 0

string:
	.ascii "Hello, World!\n"
