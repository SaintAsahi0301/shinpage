asahi = 'i am a best beer' # 문자열 string
_float = 2.23311324444434343 # 소수
_interger = 25 # 정수 ... 소수, 정수. number.
_bool = True # 불리언 (T/F)
_bool2 = False # ... 데이터 타입, 5가지.

# age = 20

# #조건문 연습
# if age < 20:
#     print("이새끼 미짜")
# elif 20<= age < 25:
#     print("동생이네? but fuckable.")
# elif age == 25:
#     print("친구노")
# else: 
#     print("fuckable")


#함수 ㅎ수학의 함수가 아닌,
#함수: Input(def 함수이름(인풋)) -> 무언가 일어남(def 블럭 안 문장) -> Output(return 키워드)
#함수: 이 3요소 중 무엇이라도 생략될 수 있음...
# def age_printer(age): # 인풋 for age
#     # 무언가 일어남( def 블럭 안 문장)
#     if age < 20:
#         print("이새끼 미짜")
#     elif 20<= age < 25:
#         print("동생이네? but fuckable.")
#     elif age == 25:
#         print("친구노")
#     else: 
#         print("fuckable")

#     #아웃풋
#     return str(age * 12) + "개월"

# 난아웃풋입니다 =age_printer(100)
# print(난아웃풋입니다)


# #파이썬내장함스
# 나는숫자 = 120
# 나는숫자일까 = str(나는숫자) #위의 것과의 차이가 존재... 두 줄 다 120으로 출력됨.

# print(나는숫자)
# print(나는숫자일까)

# print(type(나는숫자))
# print(type(나는숫자일까)) # 위의 것은 int, 아래 것은 str.


# 클래스 클라-쓰(카테고리) / 인스턴스
# 붕어빵 틀, 

class 사람:
    def __init__(self, name, age, gender, nat):
        self.name = name
        self.age = age
        self.gender = gender
        self.nat = nat

    def 자기소개(self):
        print("나의이름은", self.name, "이고요, 나이는", self.age, "성별은", self.gender, "입니다.")
        print(self.nat)
신성욱 = 사람("신성욱", "25", "달려있음.", "일본인")
최수민 = 사람("푸시", "11", "여고생.", "한국인")

신성욱.자기소개()
최수민.자기소개()









# 복습문제 [class 만들기]
# - 이름: Animal
# - 요쇠: name, eng_name, age, pet_parent
# - 메서드(함수): my_lord 라는 함수를 하나 갖고있음. (하는일: pet_parent print 하는것)

#  클래스 만들기 Class
class Animal:
    def __init__(self, name, eng_name, age, pet_parent):
        self.name = name
        self.eng_name = eng_name
        self.age = age
        self.pet_parent = pet_parent

    # 메서드 (함수 => function, 근데 함수가 특별히, class 안에있는 함수는 메서드 method 라고 따로 부름)
    def 동물이름대기(self):
        print("나는", self.name, "영어로는", self.eng_name, "그리고 나이는", self.age, "마지막으로 저의 주인은", self.pet_parent)

# 클래스 사용하기 (호출하기)
코끼리 = Animal("코끼리", "elephant", "12", "근수민")
펭귄 = Animal("펭귄", "펭귄", "111", "대통령 이명박")

# 코끼리 -> 인스턴스 Instance
# 펭귄 -> 인스턴스 Instance

# 메서드 사용하기
코끼리.동물이름대기()
펭귄.동물이름대기()


# sudo apt-get install curl
# curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash - &&\

# sudo apt-get install nodejs
# node -v 

#  sudo apt install zip