pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Jenkins sẽ tự tải image này về để chạy
        }
    }// Hoặc dùng 'agent { docker { image 'python:3.9' } }' nếu bạn muốn chạy trong container riêng

    environment {
        // Định nghĩa các biến môi trường nếu cần
        PYTHON_VERSION = '3.9'
    }

    stages {
        // Tương đương với TODO-STEP 3: Build Job
        stage('Build') {
            steps {
                echo '--- Stage: Build & Install Dependencies ---'
                
                // Checkout code từ GitHub (Jenkins sẽ tự làm nếu bạn chọn 'Pipeline from SCM')
                checkout scm

                sh '''
                    echo "Cài đặt dependencies..."
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // Tương đương với TODO-STEP 4: Test Job
        // Trong Jenkins, stage này chạy sau stage Build một cách tuần tự
        stage('Test') {
            steps {
                echo '--- Stage: Run Unit Test via Pytest ---'
                
                sh '''
                    echo "Đang chạy tests..."
                    # Chạy pytest. Lệnh '|| true' hoặc '|| exit 0' nếu bạn muốn 
                    # Jenkins không báo đỏ ngay lập tức khi test fail (nhưng thường là nên để nó đỏ)
                    pytest
                '''
            }
        }
    }

    // Các quy tắc sau khi chạy xong (tương tự logic post-build)
    post {
        always {
            echo 'Hoàn thành quy trình CI.'
        }
        success {
            echo 'Tuyệt vời! Build và Test đều thành công.'
        }
        failure {
            echo 'Có lỗi xảy ra rồi Tuan_it. Kiểm tra lại Console Output nhé!'
        }
    }
}

// Lưu ý: Đảm bảo rằng Jenkins đã được cấu hình để sử dụng Python và pytest, hoặc bạn có thể sử dụng Docker để chạy trong môi trường đã cài sẵn.