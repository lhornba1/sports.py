#checked by Dominic 11/8/18 - working!
import sports


def main():
    print('What sport would you like scores for? (type number)')
    print('1. Football\n2. Soccer\n3. Basketball\n4. Baseball')
    sport = int(input('> ')) 
    get_scores(sport)


def get_scores(sport):
    if sport == 1:
        scores = sports.get_sport(sports.FOOTBALL)
    
    elif sport == 2:
        scores = sports.get_sport(sports.SOCCER)
    elif sport == 3:
        scores = sports.get_sport(sports.BASKETBALL)
    elif sport == 4:
        scores = sports.get_sport(sports.BASEBALL)
    
    for score in scores:
        print(score)

if __name__ == '__main__':
    main()

