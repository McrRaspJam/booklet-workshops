	.global _start
_start:
	@load the memory address
	ADR R1, value

	@load the memory value
	LDR R0, [R1]
	
	@exit
	MOV R7, #1
	SWI 0

value:
	.word 72
