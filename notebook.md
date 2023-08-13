**파이썬 동시성 프로그래밍 공부**


동시성(concurrency) 프로그래밍

- 클라이언트와 서버간 통신
- 시스템 디스크 파일 읽기/쓰기
- 데이터베이스 쿼리 작업
- API 사용

병렬성(parallel  프로그래밍)

- 비디오,오디오 이미지 처리
- 컴퓨터비전
- ML
- DL

- [1. 파이썬 코루틴](#1-파이썬-코루틴)
  - [바운드와 블로킹](#바운드와-블로킹)
    - [CPU bound](#cpu-bound)
    - [IO bound](#io-bound)
    - [Blocking](#blocking)
    - [Non-Blocking](#non-blocking)
  - [동기와 비동기](#동기와-비동기)
    - [동기](#동기)
    - [비동기](#비동기)
  - [컴퓨터 구조와 os 기본](#컴퓨터-구조와-os-기본)
    - [메모리](#메모리)
      - [주메모리](#주메모리)
      - [보조메모리](#보조메모리)
    - [CPU](#cpu)
    - [입출력장치](#입출력장치)
    - [시스템버스](#시스템버스)
    - [OS](#os)
    - [프로그램](#프로그램)
    - [프로세스](#프로세스)
    - [쓰레드](#쓰레드)
      - [사용자 수준 스레드](#사용자-수준-스레드)
      - [커널 수준 스레드](#커널-수준-스레드)
  - [동시성 vs 병렬성](#동시성-vs-병렬성)
    - [동시성(concurrency)](#동시성concurrency)
    - [병렬성(Parallelism)](#병렬성parallelism)
    - [동시성 병렬성 선택](#동시성-병렬성-선택)
    - [멀티쓰레딩 문제](#멀티쓰레딩-문제)
    - [GIL(Global Interpreter Lock)](#gilglobal-interpreter-lock)
    - [Multithreading과 MultiProcessing 차이](#multithreading과-multiprocessing-차이)
    - [멀티 프로세싱은 멀티 스레딩의 단점을 막아준다.](#멀티-프로세싱은-멀티-스레딩의-단점을-막아준다)


# 1. 파이썬 코루틴

## 바운드와 블로킹

### CPU bound

> 프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한되는 것

- CPU가 한번에 한가지 일만 할 수 있기 때문에 CPU bound가 발생한다.
- 복잡한 계산을 수행하는 경우 CPU bound가 발생한다.


### IO bound
> 프로그램이 실행될 때 실행 속도가 입출력에 의해 제한되는 것

- CPU가 연산 때문에 제한되는게 아니라 입출력 때문에 제한되는 경우를 말한다.(User가 )
- 입출력 뿐만 아니라 서버간 통신을 할 때도 IO bound가 발생한다. 이 경우 Network IO bound라고 한다.


###  Blocking

> 바운드에 의해 프로그램의 실행이 중단되는 것

### Non-Blocking
> 바운드에 의해 프로그램의 실행이 중단되지 않는 것

## 동기와 비동기

### 동기
> 기본적으로 동기는 코드가 순차적으로 실행되는 것을 말한다.

### 비동기
> 코드가 순차적으로 실행되지 않는 것을 말한다.

- 요청을 먼저 보내놓고 응답을 받는다.

## 컴퓨터 구조와 os 기본

### 메모리

#### 주메모리

random access memory

랜덤 액세스 메모리(RAM)는 처리기가 어떤 순서나 순차적으로 진행하지 않고도 메모리의 모든 위치에 직접 액세스할 수 있기 때문에 "랜덤(Random)"하다고 불린다.

#### 보조메모리

### CPU

### 입출력장치

### 시스템버스

- 각 구성요소들을 연결시킴

### OS

현재 시스템을 운영하고 관리

운영체체 확인
```bash
uname -a
```

### 프로그램

코드
저장

### 프로세스

프로그램이 주 메모리로 올라와 실행되고 있는 동적인 상태

### 쓰레드
프로세스에서 CPU가 처리하는 작업의 단위

멀티스레드는 스레드가 여러개 동작하는것
멀티스레딩에서는 다수의 스레드끼리 메모리 공유와 통신이 가능
자원의 낭비를 막고 효율성을 향상시키지만 한 스레드에 문제가 생기면 전체에 영향이 간다.

#### 사용자 수준 스레드

#### 커널 수준 스레드


## 동시성 vs 병렬성

- 동시성 : Concurrency
- 병렬성 : Parallel


### 동시성(concurrency) 

> 한번에 여러 작업을 동시에 다루는 것. 기본적으로 스위칭을 하면서 여러 작업을 동시에 처리

기본적으로 여러 작업을 스위칭 하면서 동시에 처리한다는 것이 핵심이다.
동시성은 논리적 개념으로 멀티스레딩과 싱글스레드에서 모두 사용된다.
싱글코어 뿐 아니라 멀티코어에서도 각각의 코어가 동시성 사용가능


### 병렬성(Parallelism)

> 한번에 여러 작업을 병렬적으로 처리하는 것을 의미. 동시에 처리

기본적으로 물리적 개념. 병렬성이 성립하려면 기본적으로 코어가 여러개 있거나 멀티쓰레딩이여야 한다.
동시성과 공존할 수 있다. 이는 동시성이 논리적 개념이기 때문이다.

멀티스레딩에서 병렬성이 성립하려면 각각의 다른 코어에 각작의 다른 스레드가 실행되어야 한다.

Multithreading is a form of concurrent programming that can enable parallelism, but it is not necessarily parallel programming on its own.

In a multithreaded program, multiple threads are created within a process to execute different parts of the code concurrently. Each thread runs independently and shares the same memory space and resources of the process. This allows the program to execute multiple tasks concurrently, but it does not necessarily take advantage of multiple processors or cores, which is the hallmark of parallel programming.

Parallel programming, on the other hand, involves dividing a program into smaller parts that can be executed in parallel on multiple processors or cores. This can be done using techniques such as message passing, shared-memory, or distributed computing. By executing different parts of the program in parallel, it can significantly improve the performance of the program.

While multithreading can enable parallelism by allowing different threads to execute on different cores, it is not guaranteed to do so. The operating system scheduler may decide to run all the threads on a single core if there is not enough work to distribute across multiple cores or if there are other system constraints in place.

In summary, multithreading is a form of concurrent programming that can enable parallelism, but it is not synonymous with parallel programming. Parallel programming involves explicitly designing a program to take advantage of multiple processors or cores, while multithreading involves managing multiple threads within a single process.

3개의 코어로 병렬처리를 수행하면서 각각의 코어에서 동시성 처리가 가능하다.



### 동시성 병렬성 선택

The choice between concurrent programming and parallel programming depends on the specific problem that you are trying to solve and the resources available to you.

Concurrency programming is most appropriate when the problem involves **I/O-bound tasks, such as reading and writing to files or network sockets, where the tasks spend most of their time waiting for I/O operations to complete**. In this case, concurrency programming can help improve the responsiveness of the program by allowing the tasks to execute concurrently and reduce the waiting time for I/O operations.

*cpu-bound task에서 주로 병렬성 프로그래밍을 고려한다*

Parallel programming, on the other hand, is most appropriate when the problem involves **CPU-bound tasks, such as mathematical computations or data processing, where the tasks require significant processing power and can be executed simultaneously on different CPU cores or processors**. In this case, parallel programming can help improve the performance and throughput of the program by exploiting the parallelism and utilizing all available computing resources.

It is also worth noting that the choice between concurrency programming and parallel programming may also depend on the programming language and libraries being used, as well as the platform and hardware environment. Some programming languages and libraries may provide better support for concurrency or parallelism, and some platforms or hardware configurations may be more conducive to one approach over the other.

Therefore, when choosing between concurrent programming and parallel programming, it is important to consider the specific requirements of the problem, the available resources, and the characteristics of the programming language and platform being used.


왠만하면 동시성 프로그래밍을 쓰는 것이 좋다.
이는 쓰레드를 여러개 생성하고 각각의 쓰레드에 우선순위를 부여하는 것 자체가 연산비용이 들기 때문이다.

- 스레드 간 통신을 해야하기 때문에 직렬화, 역직렬화 관련하여 비용이 발생한다.

### 멀티쓰레딩 문제

멀티쓰레딩은 기본적으로는 동시성 프로그래밍이며 하나의 프로세서에 여러 스레드를 할당하는 것이다.
메모리를 공유한다.


스레드 끼리 자원을 공유함 -> 메모리를 공유함
하나의 자원을 동시에 여러 스레드가 사용할 수 있음-> 이 경우 충돌 발생
이때 하나의 스레드가 다른 스레드에 의해 차단됨

### GIL(Global Interpreter Lock)


> 한번에 한 쓰레드만 유지하는 락

한 스레드가 다른 스레드를 차단해서 제어를 얻는 것을 막아줌 -> 멀티스레딩의 잠재적인 위험(메모리 공유)으로 부터 보호

따라서 파이썬은 기본적으로 병렬성 연산을 수행하지 못한다.

**파이썬 멀티스레딩은 동시성을 사용해 io bound 에서 유용하게 사용할 수 있지만 cpu bound에서는 gil에 의해 원하는 결과를 얻을 수 없음**

동시성은 cpu bound(복잡한 계산)에서는 유용하지 않음

io-bound 컨텍스트에서는 멀티스레딩의 성능이 더 잘 나온다.


### Multithreading과 MultiProcessing 차이

Multithreading is a technique where a single process is divided into multiple threads, each of which can execute independently and concurrently within the same process. This means that multiple parts of the same program can be executed simultaneously, resulting in faster execution times. However, since all the threads share the same memory space, there can be issues with data synchronization and race conditions, which can lead to bugs and unexpected behavior.

On the other hand, multiprocessing is a technique where multiple processes are created, each of which has its own memory space and can execute independently of each other. This means that multiple programs can be executed simultaneously, allowing for true parallelism. Since each process has its own memory space, there are no issues with data synchronization or race conditions between processes. However, communication and data sharing between processes can be more complex and less efficient than in multithreading.

In summary, multithreading is a technique to achieve parallelism within a single process, while multiprocessing is a technique to achieve true parallelism by running multiple processes simultaneously. Both have their own advantages and disadvantages and are used depending on the specific needs of the program.

### 멀티 프로세싱은 멀티 스레딩의 단점을 막아준다.

## 서버 , 클라이언트, HTTP, API 이해

- 모두의 API

### TCP/IP

### API

> API의 핵심은 구현 방식을 알지 못하는 제품 또는 서비스와 통신하는 것

## 웸 스크래핑

## FastAPI Project

### ORM(Object Relational Mapper)

### ODM(Object Document Mapper)

ORM의 NoSQL 버전

ODM이란 NoSQL 데이터베이스를 사용할 때 사용하는 기술로, 객체와 문서를 매핑하는 기술이다. ORM과 유사하지만, NoSQL의 특징을 반영하여 구현되었다.

### Template Response


### fastapi DB 연결

1. 시크릿 변수 설정

2. odmantic을 사용하여 fastapi와 연결

3. models 디렉토리를 사용하여 추상화

4. book 모델 개발

5. db에 insert

