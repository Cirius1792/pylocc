---
sidebar_position: 4
---

# API Usage

You can integrate pylocc in your python scripts by adding it as dependency. 

The default language.json is distrubuted along with the package and there are commodities to load it by default. 
You can also define your own language configuration to use. 

## Configuration Factory

### Per file type

You can use the Configuration Factory to load the configuration depending on the file type.

```python 
# Create a configuration factory using the default configuration
configuration_factory = ProcessorConfigurationFactory.get_default_factory()
# If you already know the language that you are going to process, you can use the corresponding Language 
# enum to load the proper configuration and use the configuration factory to retrieve the 
# corresponding ProcessorConfiguration
file_configuration = configuration_factory.get_configuration(file_type=Language.JAVA)

with open(f, 'r', encoding='utf-8', errors='ignore', buffering=8192) as f_handle:
    report = count_locs(f_handle, file_configuration=file_configuration)
```
### Per file extension

You can use the Configuration Factory to load the configuration depending on the file extension.

```python 
# Create a configuration factory using the default configuration
configuration_factory = ProcessorConfigurationFactory.get_default_factory()
# Retrieve the extension of the file to get the proper configuration to use
# and use the configuration factory to retrieve the appropriate ProcessorConfiguration
file_configuration = configuration_factory.get_configuration(file_extension=file_extension)

with open(f, 'r', encoding='utf-8', errors='ignore', buffering=8192) as f_handle:
    report = count_locs(f_handle, file_configuration=file_configuration)
```

