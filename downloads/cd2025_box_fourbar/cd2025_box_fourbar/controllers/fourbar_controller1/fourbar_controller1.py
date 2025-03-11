from controller import Robot, Keyboard

def run_robot():
    # Create the Robot instance
    robot = Robot()
    
    # Get simulation time step
    timestep = int(robot.getBasicTimeStep())
    
    # 初始化鍵盤，並設定取樣時間為 timestep
    keyboard = Keyboard()
    keyboard.enable(timestep)

    # Get motor device
    motor = robot.getDevice('motor1')

    # Set motor for continuous rotation
    motor.setPosition(float('inf'))
    # 初始設定馬達速度為 0 (暫停狀態)
    motor.setVelocity(0.0)
    
    # 設定一個變數來追踪馬達是否在運行
    is_running = False
    
    print("模擬開始. 按下 's' 啟動馬達, 按下 'p' 暫停.")

    # Main control loop
    while robot.step(timestep) != -1:
        # 取得鍵盤輸入
        key = keyboard.getKey()
        
        # 將 key 轉換為對應的字符
        key_char = chr(key).lower() if key != -1 else ''
        
        # 使用字符直接比較
        if key_char == 's':
            is_running = True
            motor.setVelocity(1.0)
            print("馬達啟動")
            
        elif key_char == 'p':
            is_running = False
            motor.setVelocity(0.0)
            print("馬達暫停")

if __name__ == "__main__":
    run_robot()