

import argparse
from models import MultilingualImageCaptioningModel
from data_loader import get_dataloaders
from trainer import Trainer

def parse_args():
    parser = argparse.ArgumentParser(description="Train Multilingual Image Captioning Model")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to the config file')
    return parser.parse_args()

def main():
    args = parse_args()
    # Load configuration from YAML file
    config = load_config(args.config)
    
    # Initialize data loaders
    train_loader, val_loader = get_dataloaders(config)
    
    # Initialize model
    model = MultilingualImageCaptioningModel(config)
    
    # Initialize trainer
    trainer = Trainer(model, train_loader, val_loader, config)
    
    # Start training
    trainer.train()

if __name__ == '__main__':
    main()
