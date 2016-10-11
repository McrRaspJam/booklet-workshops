	.global _start
_start:
	@load the character address
	ADR R1, value

	@print
	MOV R7, #4
	MOV R0, #1
	MOV R2, #1
	SWI 0


	@exit
	MOV R7, #1
	SWI 0

value:
	.word 72
