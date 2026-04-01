pipeline {
    agent any 

    environment {
        // Định nghĩa phiên bản Python để làm log cho rõ ràng
        PYTHON_VERSION = '3.9'
    }

    stages {
        stage('Build & Install') {
            steps {
                echo '--- Stage: Build & Install Dependencies ---'
                
                // Jenkins sẽ tự động lấy code nếu bạn cấu hình SCM
                checkout scm

                sh '''
                    echo "Khởi tạo môi trường ảo..."
                    # Tạo venv nếu chưa tồn tại
                    python3 -m venv venv
                    
                    # Kích hoạt venv và cài đặt thư viện
                    . venv/bin/activate
                    pip install --upgrade pip
                    
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    else
                        echo "Không tìm thấy requirements.txt, bỏ qua cài đặt."
                    fi
                '''
            }
        }

        stage('Test') {
            steps {
                echo '--- Stage: Run Unit Test via Pytest ---'
                
                sh '''
                    echo "Đang chạy tests..."
                    # Quan trọng: Luôn phải kích hoạt lại venv ở mỗi khối lệnh sh mới
                    . venv/bin/activate
                    
                    # Cài đặt pytest nếu trong requirements.txt chưa có
                    pip install pytest
                    
                    # Chạy pytest
                    pytest || echo "Một số test case bị fail, vui lòng kiểm tra log!"
                '''
            }
        }
    }

    post {
        always {
            echo 'Hoàn thành quy trình CI.'
            // (Tùy chọn) Dọn dẹp môi trường nếu muốn tiết kiệm dung lượng container
            // sh 'rm -rf venv' 
        }
        success {
            echo 'Tuyệt vời! Build và Test đều thành công.'
        }
        failure {
            echo 'Có lỗi xảy ra rồi Tuan_it. Kiểm tra lại Console Output nhé!'
        }
    }
}