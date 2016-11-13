# for cheking the correctness of the answers at the end of los

Final_A = 16
Final_B = 16
Final_C = 15
Final_D = 15
Final_E = 11
Final_F = 12



def printVars(A,B,C,D,E,F):
	return "A "+str(A)+" B "+str(B)+" C "+str(C)+" D "+str(D)+" E "+str(E)+" F "+str(F)+"\n"

def Updated(t, var, A, B, C, D, E, F, val):
	return "<T"+str(t) + ","+var+","+str(val)+"> " + printVars(A,B,C,D,E,F)


def UndoOne(iA, iB, iC, iD, iE, iF):

	A = iA 
	B = iB
	C = iC
	D = iD
	E = iC
	F = iD


	f1 = open('../logs/1.txt_undo','wa+')
	Output = []
	Output.append("<start T1> " + printVars(A,B,C,D,E,F))
	t1=iA
	Output.append("<start T2> " + printVars(A,B,C,D,E,F))
	t21 = iC
	Output.append("<start T3> " + printVars(A,B,C,D,E,F))
	t3 = iD

	t1 = t1*2
	t22 = iD
	t3 = t3+1

	A = t1
	Output.append(Updated(1, "A", A, B, C, D, E, F, A))
	t21 = t21 + t22
	E = t3
	Output.append(Updated(3, "E", A, B, C, D, E, F, E))

	t1 = B
	C = t21
	Output.append(Updated(2, "C", A, B, C, D, E, F, C))
	t3 = E

	t1=t1*2
	t21=t21-t22
	t3=t3+1

	B = t1
	Output.append(Updated(1, "B", A, B, C, D, E, F, B))
	t21 = t21 + t22
	F = t3
	Output.append(Updated(3, "F", A, B, C, D, E, F, F))

	Output.append("<commit T1> " + printVars(A, B, C, D, E, F))
	D = t21
	Output.append(Updated(2, "D", A, B, C, D, E, F, D))
	Output.append("<commit T3> " + printVars(A, B, C, D, E, F))
	Output.append("<commit T2> " + printVars(A, B, C, D, E, F))

	if(Final_A == A and Final_B == B and Final_C == C and Final_D == D and Final_E == E and Final_F == F):
		Output.append("1\n")

	f1.writelines(Output)
	f1.close()

def RedoOne(iA, iB, iC, iD, iE, iF):
	A = iA 
	B = iB
	C = iC
	D = iD
	E = iC
	F = iD


	f1 = open('../logs/1.txt_redo','wa+')
	Output = []
	Output.append("<start T1> " + printVars(A,B,C,D,E,F))
	t1=iA
	Output.append("<start T2> " + printVars(A,B,C,D,E,F))
	t21 = iC
	Output.append("<start T3> " + printVars(A,B,C,D,E,F))
	t3 = iD

	t1 = t1*2
	t22 = iD
	t3 = t3+1

	A = t1
	Output.append(Updated(1, "A", A, B, C, D, E, F, A))
	t21 = t21 + t22
	E = t3
	Output.append(Updated(3, "E", A, B, C, D, E, F, E))

	t1 = B
	C = t21
	Output.append(Updated(2, "C", A, B, C, D, E, F, C))
	t3 = E

	t1=t1*2
	t21=t21-t22
	t3=t3+1

	B = t1
	Output.append(Updated(1, "B", A, B, C, D, E, F, B))
	Output.append("<commit T1> " + printVars(A, B, C, D, E, F))
	t21 = t21 + t22
	F = t3
	Output.append(Updated(3, "F", A, B, C, D, E, F, F))
	Output.append("<commit T3> " + printVars(A, B, C, D, E, F))

	D = t21
	Output.append(Updated(2, "D", A, B, C, D, E, F, D))
	Output.append("<commit T2> " + printVars(A, B, C, D, E, F))


	if(Final_A == A and Final_B == B and Final_C == C and Final_D == D and Final_E == E and Final_F == F):
			Output.append("1\n")
			
	f1.writelines(Output)
	f1.close()

def RedoUndoOne(iA, iB, iC, iD, iE, iF):
	A = iA 
	B = iB
	C = iC
	D = iD
	E = iC
	F = iD


	f1 = open('../logs/1.txt_undoredo','wa+')
	Output = []
	Output.append("<start T1> " + printVars(A,B,C,D,E,F))
	t1=iA
	Output.append("<start T2> " + printVars(A,B,C,D,E,F))
	t21 = iC
	Output.append("<start T3> " + printVars(A,B,C,D,E,F))
	t3 = iD

	t1 = t1*2
	t22 = iD
	t3 = t3+1

	A = t1
	Output.append(Updated(1, "A", A, B, C, D, E, F, A))
	t21 = t21 + t22
	E = t3
	Output.append(Updated(3, "E", A, B, C, D, E, F, E))

	t1 = B
	C = t21
	Output.append(Updated(2, "C", A, B, C, D, E, F, C))
	t3 = E

	t1=t1*2
	t21=t21-t22
	t3=t3+1

	B = t1
	Output.append(Updated(1, "B", A, B, C, D, E, F, B))
	t21 = t21 + t22
	F = t3
	Output.append(Updated(3, "F", A, B, C, D, E, F, F))
	Output.append("<commit T1> " + printVars(A, B, C, D, E, F))
	

	D = t21
	Output.append(Updated(2, "D", A, B, C, D, E, F, D))
	Output.append("<commit T3> " + printVars(A, B, C, D, E, F))
	Output.append("<commit T2> " + printVars(A, B, C, D, E, F))

	if Final_A == A and Final_B == B and Final_C == C and Final_D == D and Final_E == E and Final_F == F:
		Output.append("1\n")
			

	f1.writelines(Output)
	f1.close()


UndoOne(8,8,5,10,5,10)
RedoOne(8,8,5,10,5,10)
RedoUndoOne(8,8,5,10,5,10)