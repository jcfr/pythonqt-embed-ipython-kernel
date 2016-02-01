

from IPython.utils.frame import extract_module_locals

embed_kernel_done = False

def embed_kernel(module=None, local_ns=None, **kwargs):
    """Embed and start an IPython kernel in a given scope.

    If you don't want the kernel to initialize the namespace
    from the scope of the surrounding function,
    and/or you want to load full IPython configuration,
    you probably want `IPython.start_kernel()` instead.

    Parameters
    ----------
    module : ModuleType, optional
        The module to load into IPython globals (default: caller)
    local_ns : dict, optional
        The namespace to load into IPython user namespace (default: caller)

    kwargs : various, optional
        Further keyword args are relayed to the IPKernelApp constructor,
        allowing configuration of the Kernel.  Will only have an effect
        on the first embed_kernel call for a given process.
    """

    global embed_kernel_done
    if embed_kernel_done:
        return
    embed_kernel_done = True

    (caller_module, caller_locals) = extract_module_locals(1)
    if module is None:
        module = caller_module
    if local_ns is None:
        local_ns = caller_locals

    # Only import .zmq when we really need it
    from .embed import embed_kernel as real_embed_kernel
    real_embed_kernel(module=module, local_ns=local_ns, **kwargs)
