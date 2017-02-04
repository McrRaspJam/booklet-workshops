	.global _start
_start:
	@set two registers
	MOV R0, #65
	MOV R1, #37

	@store addition in R0
	ADD R0, R0, R1

	@exit
	MOV R7, #1
	SWI 0
	

