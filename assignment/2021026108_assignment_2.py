from OpenGL.GL import *
from glfw.GLFW import *
import glm
g_vertex_shader_src = '''
#version 330 core

// input vertex position. its attribute index is 0.
layout (location = 0) in vec3 vin_pos; 

void main()
{
    gl_Position = vec4(vin_pos.x, vin_pos.y, vin_pos.z, 1.0);

}
'''

#input skip, ouput fragment color
g_fragment_shader_src = '''
#version 330 core

out vec4 FragColor;

void main()
{
    FragColor = vec4(1.0f, 0.0f, 0.0f, 1.0f);
}
'''

def load_shaders(vertex_shader_source, fragment_shader_source):
    # build and compile our shader program
    # ------------------------------------
    
    # vertex shader 
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)    # create an empty shader object
    glShaderSource(vertex_shader, vertex_shader_source) # provide shader source code
    glCompileShader(vertex_shader)                      # compile the shader object
    
    # check for shader compile errors
    success = glGetShaderiv(vertex_shader, GL_COMPILE_STATUS)
    if (not success):
        infoLog = glGetShaderInfoLog(vertex_shader)
        print("ERROR::SHADER::VERTEX::COMPILATION_FAILED\n" + infoLog.decode())
        
    # fragment shader
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)    # create an empty shader object
    glShaderSource(fragment_shader, fragment_shader_source) # provide shader source code
    glCompileShader(fragment_shader)                        # compile the shader object
    
    # check for shader compile errors
    success = glGetShaderiv(fragment_shader, GL_COMPILE_STATUS)
    if (not success):
        infoLog = glGetShaderInfoLog(fragment_shader)
        print("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n" + infoLog.decode())

    # link shaders
    shader_program = glCreateProgram()               # create an empty program object
    glAttachShader(shader_program, vertex_shader)    # attach the shader objects to the program object
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)                    # link the program object

    # check for linking errors
    success = glGetProgramiv(shader_program, GL_LINK_STATUS)
    if (not success):
        infoLog = glGetProgramInfoLog(shader_program)
        print("ERROR::SHADER::PROGRAM::LINKING_FAILED\n" + infoLog.decode())
        
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return shader_program    # return the shader program


def key_callback(window, key, scancode, action, mods):
    if key==GLFW_KEY_ESCAPE and action==GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE);
        
def main():
    # initialize glfw
    if not glfwInit():
        return
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3) # OpenGL 3.3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3)
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE) # Do notallow legacy OpenGl API calls
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE) # for macOS 호환성 모드 활성화
    # create a window and OpenGL context
    window = glfwCreateWindow(800, 800, '2021026108', None, None) #윈도우 생성
    if not window: #윈도우 생성 실패시 종료
        glfwTerminate()
        return
    glfwMakeContextCurrent(window); #opengl의 렌더링 컨텍스트로 설정
    # register key callback for escape key
    glfwSetKeyCallback(window, key_callback) #key 입력 발생시 처리
    
    shader_program = load_shaders(g_vertex_shader_src, g_fragment_shader_src)
    vertices = glm.array(glm.float32,
        -0.5,-0.5,0.0,
        0.5,-0.5,0.0,
        -0.5,0.5,0.0,
        0.5,0.5,0.0
    )
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices.ptr, GL_STATIC_DRAW)
    glVertexAttribPointer(0,3,GL_FLOAT, GL_FALSE, 3*glm.sizeof(glm.float32),None)
    glEnableVertexAttribArray(0)
    
    while not glfwWindowShouldClose(window): #창 닫힐 때까지 반복
        # render 함수 추가
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader_program)
        glBindVertexArray(VAO)
        glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)
        glfwSwapBuffers(window)
        
        glfwPollEvents()
    glfwTerminate()
    
if __name__ == "__main__": #이 파일을 직접 실행할 때만 실행 import 해서 실행시 main 함수가 호출되지 않음
    main()