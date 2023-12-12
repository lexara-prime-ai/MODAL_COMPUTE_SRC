import platform
import modal_compute
import modal

PYTHON_VERSION: str = platform.python_version()

# Create modal stub
stub = modal.Stub("REMOTE_WORKER")

@stub.function()
def invoke_rust_lib():
    print("Running external library...")
    # Some random value
    output = modal_compute.square_as_root(42)
    print("DEMO OUTPUT: ", output)

@stub.local_entrypoint()
def main():
    print("\nSYSTEM_INFO: ", PYTHON_VERSION)
    invoke_rust_lib.remote()
