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

> 한번에 여러 작업을 병렬적으로 처리하는 것을 의미. 기본적으로 동시에 처리

기본적으로 물리적 개념. 병렬성이 성립하려면 기본적으로 코어가 여러개 있거나 멀티쓰레딩이여야 한다.
동시성과 공존할 수 있다. 이는 동시성이 논리적 개념이기 때문이다.

3개의 코어로 병렬처리를 수행하면서 각각의 코어에서


### 동시성 병렬성 선택

The choice between concurrent programming and parallel programming depends on the specific problem that you are trying to solve and the resources available to you.

Concurrency programming is most appropriate when the problem involves **I/O-bound tasks, such as reading and writing to files or network sockets, where the tasks spend most of their time waiting for I/O operations to complete**. In this case, concurrency programming can help improve the responsiveness of the program by allowing the tasks to execute concurrently and reduce the waiting time for I/O operations.

Parallel programming, on the other hand, is most appropriate when the problem involves **CPU-bound tasks, such as mathematical computations or data processing, where the tasks require significant processing power and can be executed simultaneously on different CPU cores or processors**. In this case, parallel programming can help improve the performance and throughput of the program by exploiting the parallelism and utilizing all available computing resources.

It is also worth noting that the choice between concurrency programming and parallel programming may also depend on the programming language and libraries being used, as well as the platform and hardware environment. Some programming languages and libraries may provide better support for concurrency or parallelism, and some platforms or hardware configurations may be more conducive to one approach over the other.

Therefore, when choosing between concurrent programming and parallel programming, it is important to consider the specific requirements of the problem, the available resources, and the characteristics of the programming language and platform being used.


왠만하면 동시성 프로그래밍을 쓰는 것이 좋다.
이는 쓰레드를 여러개 생성하고 각각의 쓰레드에 우선순위를 부여하는 것 자체가 연산비용이 들기 때문이다.

### 멀티쓰레딩 문제

스레드 끼리 자원을 공유함
하나의 자원을 동시에 여러 스레드가 가용

### GIL(Global interpreter lock)

> 한번에 한 쓰레드만 유지하는 락

한 스레드가 다른 스레드를 차단해서 제어를 얻는 것을 막아줌 -> 

따라서 파이썬은 기본적으로 병렬성 연산을 수행하지 못한다.


멀티쓰레드는 쓰레드들 끼리 자원을 공유하기 때문에 한쪽에서 문