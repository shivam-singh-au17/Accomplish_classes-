

def findQUEUE (NoOfPeople, NoOfFrontPeople, NoOfBehindPeople):

	return NoOfPeople - max(NoOfFrontPeople + 1, NoOfPeople - NoOfBehindPeople) + 1;


if __name__ == "__main__":

    NoOfPeople  = int(input())
    NoOfFrontPeople  = int(input())
    NoOfBehindPeople  = int(input())

    ans = findQUEUE (NoOfPeople, NoOfFrontPeople, NoOfBehindPeople)
    print(ans)

