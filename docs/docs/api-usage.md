---
sidebar_position: 4
---

# API Usage

## Configuration Factory
```python 
# Create a configuration factory using the default configuration
configuration_factory = ProcessorConfigurationFactory.get_default_factory()
# Retrieve the extension of the file to get the proper configuration to use
# and use the configuration factory to retrieve the appropriate ProcessorConfiguration
file_configuration = configuration_factory.get_configuration(file_extension)

processor = Processor()
with open(f, 'r', encoding='utf-8', errors='ignore', buffering=8192) as f_handle:
    report = processor.process(f_handle, file_configuration=file_configuration)
```
The languages supported by the default configuration are listed in the "Supported Languages" page.
