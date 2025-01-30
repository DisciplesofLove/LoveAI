Love AI Compute Node - README

Welcome to the Love AI Compute Node repository! This project is designed to enable a decentralized AI infrastructure, allowing users to contribute compute power for processing AI inference tasks. This system supports DeepSeek V3 and utilizes a hybrid decentralized storage and compute model.

🚀 Overview

Love AI is a decentralized AI network that allows compute nodes to process AI inference workloads. The system works by:

Chunking & storing AI models on IPFS/Filecoin.

Fetching and verifying model integrity using Merkle Trees.

Running AI inference on decentralized compute nodes.

Routing AI tasks via the Load Balancer.

Submitting Proof of Inference (PoI) to ensure valid computations.

Earning $Joy Token rewards for node operators.

This repo includes everything needed to set up, deploy, and maintain a compute node in the Love AI ecosystem.

📌 Features

✅ Decentralized AI Execution – Nodes fetch and run DeepSeek V3 models.✅ Distributed Storage – AI models are stored on IPFS/Filecoin.✅ Optimized Load Balancing – Routes tasks to the best available compute node.✅ Proof of Inference (PoI) – Ensures results are verifiable.✅ Auto-Scaling – Nodes can be dynamically added or removed.✅ Earn $Joy Token – Compute nodes receive rewards for AI tasks.

🛠️ System Requirements

Minimum Requirements

CPU: 8-Core Processor (Intel/AMD)

RAM: 16GB+

GPU: NVIDIA RTX 3090 / A100 (or equivalent AMD GPU)

Storage: 500GB SSD

Internet: 50 Mbps+ stable connection

Recommended for High-Performance Nodes

CPU: 16-Core or more

RAM: 32GB+

GPU: Multiple A100 GPUs / AMD MI200

Storage: 1TB NVMe SSD

Network: Gigabit fiber-optic connection

🛠️ Installation & Setup

1️⃣ Install Dependencies

sudo apt update && sudo apt install -y docker docker-compose python3-pip
pip3 install torch transformers ipfshttpclient flask pyyaml requests

2️⃣ Install & Configure IPFS

wget https://dist.ipfs.tech/kubo/latest/kubo-linux-amd64.tar.gz
tar -xvzf kubo-linux-amd64.tar.gz
sudo mv ipfs /usr/local/bin
ipfs init
ipfs daemon

3️⃣ Clone & Set Up Love AI Node

git clone https://github.com/loveai-network/loveai-node.git
cd loveai-node

4️⃣ Start the Node

docker-compose up -d

To check node logs:

docker logs -f loveai-node

🖥️ Node Responsibilities

🔗 Fetching AI Model Chunks – The node retrieves encrypted model chunks from IPFS/Filecoin.

✅ Verifying Model Integrity – Using Merkle Trees, the node checks that chunks match the on-chain Merkle Root.

💡 Running AI Inference – The node assembles the model and executes AI tasks.

🔏 Submitting Proof of Inference (PoI) – The node generates a cryptographic proof that the computation was correctly performed.

💰 Earning $Joy Token – Nodes receive tokens based on the number of valid AI tasks completed.

📂 Repo Structure

loveai-node/
│── api_gateway.py          # Central API entry point
│── data_router.py          # Routes data between storage and compute nodes
│── deepseek_inference.py   # Runs DeepSeek V3 inference
│── docker-compose.yml      # Container setup
│── ipfs_manager.py         # Handles IPFS storage for model chunks
│── load_balancer.py        # Routes AI requests to the best compute node
│── metadata_manager.py     # Manages Merkle Tree for model integrity
│── model_chunker.py        # Splits DeepSeek V3 into storage chunks
│── model_loader.py         # Fetches & verifies chunks, reassembles AI model
│── network_discovery.py    # Finds new compute nodes
│── node_config.yaml        # Node settings
│── node_health_checker.py  # Removes inactive compute nodes
│── proof_of_inference.py   # Verifies AI computations
│── requirements.txt        # Required dependencies
│── security_manager.py     # Encrypts & verifies AI execution data
│── task_handler.py         # Manages AI requests
│── task_manager.py         # Distributes AI tasks
│── tests/
│   ├── test_ai_requests.py
│   ├── test_data_router.py
│   ├── test_load_balancer.py
│   ├── test_model_integrity.py
│   └── test_security.py

📈 Scaling Up: Running Multiple Nodes

1️⃣ Using Docker Swarm

docker swarm init
docker stack deploy -c docker-compose.yml loveai

2️⃣ Using Kubernetes (K8s)

kubectl apply -f k8s-node-deployment.yaml

🔄 Updating & Maintaining Your Node

Check Compute Node Performance

docker stats

Update the Node

cd loveai-node
git pull origin main
docker-compose up --build -d

Restart Node

docker restart loveai-node

💰 Rewards & Governance

1️⃣ Earn $Joy Token for Running a Node

Compute nodes receive rewards based on:
✅ Number of AI tasks completed✅ Compute power provided✅ Proof of Inference (PoI) validation

2️⃣ Participate in Governance (LOVE DAO)

Vote on AI policies and improvements in Love AI Governance.

🚀 Get Started Today!

Run a Love AI node, contribute to decentralized AI, and earn $Joy Token rewards!

📌 Join the network & start your node today! 🚀


