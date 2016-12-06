from collections import defaultdict
cuboSemantico = defaultdict(lambda :defaultdict(lambda :defaultdict(int)))
"""
	==TIPOS
	ENTERO		 0
	FLOTANTE	 1
	TEXTO	 	 2
	BOLEANO	 	 3
	ERROR		-1

	==OPERADOR
	+		0
	-		1
	*		2
	/		3
	%		4
	&		5
	|		6
	<		7
	>		8
	==		9
	!=		10
	>=		11
	<=		12
	=		13
"""


# INT
cuboSemantico[0][0][0] = 0; # int + int = int
cuboSemantico[0][1][0] = -1; # int + double = error
cuboSemantico[0][2][0] = -1; # int + string = error
cuboSemantico[0][3][0] = -1; # int + bool = error

cuboSemantico[0][0][1] = 0; # int - int = int
cuboSemantico[0][1][1] = -1; # int - double = error
cuboSemantico[0][2][1] = -1; # int - string = error
cuboSemantico[0][3][1] = -1; # int - bool = error

cuboSemantico[0][0][2] = 0; # int * int = int
cuboSemantico[0][1][2] = -1; # int * double = error
cuboSemantico[0][2][2] = -1; # int * string = error
cuboSemantico[0][3][2] = -1; # int * bool = error

cuboSemantico[0][0][3] = 0; # int / int = int
cuboSemantico[0][1][3] = -1; # int / double = error
cuboSemantico[0][2][3] = -1; # int / string = error
cuboSemantico[0][3][3] = -1; # int / bool = error

cuboSemantico[0][0][4] = 0; # int % int = int
cuboSemantico[0][1][4] = -1; # int % double = error
cuboSemantico[0][2][4] = -1; # int % string = error
cuboSemantico[0][3][4] = -1; # int % bool = error

cuboSemantico[0][0][5] = -1; # int & int = error
cuboSemantico[0][1][5] = -1; # int & double = error
cuboSemantico[0][2][5] = -1; # int & string = error
cuboSemantico[0][3][5] = -1; # int & bool = error

cuboSemantico[0][0][6] = -1; # int | int = error
cuboSemantico[0][1][6] = -1; # int | double = error
cuboSemantico[0][2][6] = -1; # int | string = error
cuboSemantico[0][3][6] = -1; # int | bool = error

cuboSemantico[0][0][7] = 3; # int < int = bool
cuboSemantico[0][1][7] = -1; # int < double = error
cuboSemantico[0][2][7] = -1; # int < string = error
cuboSemantico[0][3][7] = -1; # int < bool = error

cuboSemantico[0][0][8] = 3; # int > int = bool
cuboSemantico[0][1][8] = -1; # int > double = error
cuboSemantico[0][2][8] = -1; # int > string = error
cuboSemantico[0][3][8] = -1; # int > bool = error

cuboSemantico[0][0][9] = 3; # int == int = bool
cuboSemantico[0][1][9] = -1; # int == double = error
cuboSemantico[0][2][9] = -1; # int == string = error
cuboSemantico[0][3][9] = -1; # int == bool = error

cuboSemantico[0][0][10] = 3; # int != int = bool
cuboSemantico[0][1][10] = -1; # int != double = error
cuboSemantico[0][2][10] = -1; # int != string = error
cuboSemantico[0][3][10] = -1; # int != bool = error

cuboSemantico[0][0][11] = 3; # int >= int = bool
cuboSemantico[0][1][11] = -1; # int >= double = error
cuboSemantico[0][2][11] = -1; # int >= string = error
cuboSemantico[0][3][11] = -1; # int >= bool = error

cuboSemantico[0][0][12] = 3; # int <= int = bool
cuboSemantico[0][1][12] = -1; # int <= double = error
cuboSemantico[0][2][12] = -1; # int <= string = error
cuboSemantico[0][3][12] = -1; # int <= bool = error

cuboSemantico[0][0][13] = 1; # int = int
cuboSemantico[0][1][13] = -1; # int = double
cuboSemantico[0][2][13] = -1; # int = string
cuboSemantico[0][3][13] = -1; # int = bool

# DOUBLE
cuboSemantico[1][0][0] = -1; # double + int = error
cuboSemantico[1][1][0] = 1; # double + double = double
cuboSemantico[1][2][0] = -1; # double + string = error
cuboSemantico[1][3][0] = -1; # double + bool = error

cuboSemantico[1][0][1] = -1; # double - int = error
cuboSemantico[1][1][1] = 1; # double - double = double
cuboSemantico[1][2][1] = -1; # double - string = error
cuboSemantico[1][3][1] = -1; # double - bool = error

cuboSemantico[1][0][2] = -1; # double * int = error
cuboSemantico[1][1][2] = 1; # double * double = double
cuboSemantico[1][2][2] = -1; # double * string = error
cuboSemantico[1][3][2] = -1; # double * bool = error

cuboSemantico[1][0][3] = -1; # double / int = error
cuboSemantico[1][1][3] = 1; # double / double = double
cuboSemantico[1][2][3] = -1; # double / string = error
cuboSemantico[1][3][3] = -1; # double / bool = error

cuboSemantico[1][0][4] = -1; # double % int = error
cuboSemantico[1][1][4] = 0; # double % double = int
cuboSemantico[1][2][4] = -1; # double % string = error
cuboSemantico[1][3][4] = -1; # double % bool = error

cuboSemantico[1][0][5] = -1; # double & int = error
cuboSemantico[1][1][5] = -1; # double & double = error
cuboSemantico[1][2][5] = -1; # double & string = error
cuboSemantico[1][3][5] = -1; # double & bool = error

cuboSemantico[1][0][6] = -1; # double | int = error
cuboSemantico[1][1][6] = -1; # double | double = error
cuboSemantico[1][2][6] = -1; # double | string = error
cuboSemantico[1][3][6] = -1; # double | bool = error

cuboSemantico[1][0][7] = -1; # double < int = error
cuboSemantico[1][1][7] = 3; # double < double = bool
cuboSemantico[1][2][7] = -1; # double < string = string
cuboSemantico[1][3][7] = -1; # double < bool = string

cuboSemantico[1][0][8] = -1; # double > int = error
cuboSemantico[1][1][8] = 3; # double > double = bool
cuboSemantico[1][2][8] = -1; # double > string = error
cuboSemantico[1][3][8] = -1; # double > bool = error

cuboSemantico[1][0][9] = -1; # double == int = error
cuboSemantico[1][1][9] = 3; # double == double = bool
cuboSemantico[1][2][9] = -1; # double == string = error
cuboSemantico[1][3][9] = -1; # double == bool = error

cuboSemantico[1][0][10] = -1; # double != int = error
cuboSemantico[1][1][10] = 3; # double != double = double
cuboSemantico[1][2][10] = -1; # double != string = error
cuboSemantico[1][3][10] = -1; # double != bool = error

cuboSemantico[1][0][11] = -1; # double >= int = error
cuboSemantico[1][1][11] = 3; # double >= double = bool
cuboSemantico[1][2][11] = -1; # double >= string = error
cuboSemantico[1][3][11] = -1; # double >= bool = error

cuboSemantico[1][0][12] = -1; # double <= int = error
cuboSemantico[1][1][12] = 3; # double <= double = bool
cuboSemantico[1][2][12] = -1; # double <= string = error
cuboSemantico[1][3][12] = -1; # double <= bool = error

cuboSemantico[1][0][13] = -1; # double = int
cuboSemantico[1][1][13] = 1; # double = double
cuboSemantico[1][2][13] = -1; # double = string
cuboSemantico[1][3][13] = -1; # double = bool

# STRING
cuboSemantico[2][0][0] = -1; # string + int = error
cuboSemantico[2][1][0] = -1; # string + double = error
cuboSemantico[2][2][0] = 2; # string + string = string
cuboSemantico[2][3][0] = -1; # string + bool = error

cuboSemantico[2][0][1] = -1; # string - int = error
cuboSemantico[2][1][1] = -1; # string - double = error
cuboSemantico[2][2][1] = -1; # string - string = error
cuboSemantico[2][3][1] = -1; # string - bool = error

cuboSemantico[2][0][2] = -1; # string * int = error
cuboSemantico[2][1][2] = -1; # string * double = error
cuboSemantico[2][2][2] = -1; # string * string = error
cuboSemantico[2][3][2] = -1; # string * bool = error

cuboSemantico[2][0][3] = -1; # string / int = error
cuboSemantico[2][1][3] = -1; # string / double = error
cuboSemantico[2][2][3] = -1; # string / string = error
cuboSemantico[2][3][3] = -1; # string / bool = error

cuboSemantico[2][0][4] = -1; # string % int = error
cuboSemantico[2][1][4] = -1; # string % double = error
cuboSemantico[2][2][4] = -1; # string % string = error
cuboSemantico[2][3][4] = -1; # string % bool = error

cuboSemantico[2][0][5] = -1; # string & int = error
cuboSemantico[2][1][5] = -1; # string & double = error
cuboSemantico[2][2][5] = -1; # string & string = error
cuboSemantico[2][3][5] = -1; # string & bool = error

cuboSemantico[2][0][6] = -1; # string | int = error
cuboSemantico[2][1][6] = -1; # string | double = error
cuboSemantico[2][2][6] = -1; # string | string = error
cuboSemantico[2][3][6] = -1; # string | bool = error

cuboSemantico[2][0][7] = -1; # string < int = error
cuboSemantico[2][1][7] = -1; # string < double = error
cuboSemantico[2][2][7] = -1; # string < string = error
cuboSemantico[2][3][7] = -1; # string < bool = error

cuboSemantico[2][0][8] = -1; # string > int = error
cuboSemantico[2][1][8] = -1; # string > double = error
cuboSemantico[2][2][8] = -1; # string > string = error
cuboSemantico[2][3][8] = -1; # string > bool = error

cuboSemantico[2][0][9] = -1; # string == int = error
cuboSemantico[2][1][9] = -1; # string == double = error
cuboSemantico[2][2][9] = 3; # string == string = bool
cuboSemantico[2][3][9] = -1; # string == bool = error

cuboSemantico[2][0][10] = -1; # string != int = error
cuboSemantico[2][1][10] = -1; # string != double = error
cuboSemantico[2][2][10] = 3; # string != string = bool
cuboSemantico[2][3][10] = -1; # string != bool = error

cuboSemantico[2][0][11] = -1; # string >= int = error
cuboSemantico[2][1][11] = -1; # string >= double = error
cuboSemantico[2][2][11] = -1; # string >= string = error
cuboSemantico[2][3][11] = -1; # string >= bool = error

cuboSemantico[2][0][12] = -1; # string <= int = error
cuboSemantico[2][1][12] = -1; # string <= double = error
cuboSemantico[2][2][12] = -1; # string <= string = error
cuboSemantico[2][3][12] = -1; # string <= bool = error

cuboSemantico[2][0][13] = -1; # string = int
cuboSemantico[2][1][13] = -1; # string = double
cuboSemantico[2][2][13] = 2; # string = string
cuboSemantico[2][3][13] = -1; # string = bool

# BOOL
cuboSemantico[3][0][0] = -1; # bool + int = error
cuboSemantico[3][1][0] = -1; # bool + double = error
cuboSemantico[3][2][0] = -1; # bool + string = error
cuboSemantico[3][3][0] = -1; # bool + bool = error

cuboSemantico[3][0][1] = -1; # bool - int = error
cuboSemantico[3][1][1] = -1; # bool - double = error
cuboSemantico[3][2][1] = -1; # bool - string = error
cuboSemantico[3][3][1] = -1; # bool - bool = error

cuboSemantico[3][0][2] = -1; # bool * int = error
cuboSemantico[3][1][2] = -1; # bool * double = error
cuboSemantico[3][2][2] = -1; # bool * string = error
cuboSemantico[3][3][2] = -1; # bool * bool = error

cuboSemantico[3][0][3] = -1; # bool / int = error
cuboSemantico[3][1][3] = -1; # bool / double = error
cuboSemantico[3][2][3] = -1; # bool / string = error
cuboSemantico[3][3][3] = -1; # bool / bool = error

cuboSemantico[3][0][4] = -1; # bool % int = error
cuboSemantico[3][1][4] = -1; # bool % double = error
cuboSemantico[3][2][4] = -1; # bool % string = error
cuboSemantico[3][3][4] = -1; # bool % bool = error

cuboSemantico[3][0][5] = -1; # bool & int = error
cuboSemantico[3][1][5] = -1; # bool & double = error
cuboSemantico[3][2][5] = -1; # bool & string = error
cuboSemantico[3][3][5] = 3;  # bool & bool = bool

cuboSemantico[3][0][6] = -1; # bool | int = error
cuboSemantico[3][1][6] = -1; # bool | double = error
cuboSemantico[3][2][6] = -1; # bool | string = error
cuboSemantico[3][3][6] = 3;  # bool | bool = bool

cuboSemantico[3][0][7] = -1; # bool < int = error
cuboSemantico[3][1][7] = -1; # bool < double = error
cuboSemantico[3][2][7] = -1; # bool < string = error
cuboSemantico[3][3][7] = -1; # bool < bool = error

cuboSemantico[3][0][8] = -1; # bool > int = error
cuboSemantico[3][1][8] = -1; # bool > double = error
cuboSemantico[3][2][8] = -1; # bool > string = error
cuboSemantico[3][3][8] = -1; # bool > bool = error

cuboSemantico[3][0][9] = -1; # bool == int = error
cuboSemantico[3][1][9] = -1; # bool == double = error
cuboSemantico[3][2][9] = -1; # bool == string = error
cuboSemantico[3][3][9] = 3; # bool == bool = bool

cuboSemantico[3][0][10] = -1; # bool != int = error
cuboSemantico[3][1][10] = -1; # bool != double = error
cuboSemantico[3][2][10] = -1; # bool != string = error
cuboSemantico[3][3][10] = 3; # bool != bool = bool

cuboSemantico[3][0][11] = -1; # bool >= int = error
cuboSemantico[3][1][11] = -1; # bool >= double = error
cuboSemantico[3][2][11] = -1; # bool >= string = error
cuboSemantico[3][3][11] = -1; # bool >= bool = error

cuboSemantico[3][0][12] = -1; # bool <= int = error
cuboSemantico[3][1][12] = -1; # bool <= double = error
cuboSemantico[3][2][12] = -1; # bool <= string = error
cuboSemantico[3][3][12] = -1; # bool <= bool = error

cuboSemantico[3][0][13] = -1; # bool = int
cuboSemantico[3][1][13] = -1; # bool = double
cuboSemantico[3][2][13] = -1; # bool = string
cuboSemantico[3][3][13] = 3; # bool = bool
