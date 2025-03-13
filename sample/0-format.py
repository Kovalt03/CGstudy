from OpenGL.GL import *
from glfw.GLFW import *

def main():
    # initialize glfw
    if not glfwInit():
        return
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3) # OpenGL 3.3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE) # Do notallow legacy OpenGl API calls
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE) # for macOS 호환성 모드 활성화
    # create a window and OpenGL context
    window = glfwCreateWindow(800, 800, '1-first-gl-program', None, None) #윈도우 생성
    if not window: #윈도우 생성 실패시 종료
        glfwTerminate()
        return
    glfwMakeContextCurrent(window); #opengl의 렌더링 컨텍스트로 설정
    # register key callback for escape key
    glfwSetKeyCallback(window, key_callback) #key 입력 발생시 처리
    while not glfwWindowShouldClose(window): #창 닫힐 때까지 반복
        # render 함수 추가

        glfwSwapBuffers(window)
        
        glfwPollEvents()
    glfwTerminate()
    
if __name__ == "__main__": #이 파일을 직접 실행할 때만 실행 import 해서 실행시 main 함수가 호출되지 않음
    main()