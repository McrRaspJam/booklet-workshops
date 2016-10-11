	.global _start
_start:
	@set a register
	MOV R0, #65
	MOV R1, #105
	ADD R0, R0, R1

	@exit
	MOV R7, #1
	SWI 0
	

