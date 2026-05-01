
# Wallet Security Guide for Fuel Agent Kit

This guide provides best practices for securely handling wallet-related operations in the Fuel Agent Kit.

## Storing Mnemonics

Mnemonics (seed phrases) are the foundation of your wallet security. Follow these guidelines:

### Never Hardcode Mnemonics
- **Never** store mnemonics directly in your codebase or configuration files
- Mnemonics should never be committed to version control
- Use environment variables or secure secret management systems instead

### Secure Storage Options
1. **Environment Variables**: Store mnemonics in environment variables
   ```bash
   export WALLET_MNEMONIC="your-mnemonic-here"
   ```
   Then access them in your code:
   ```typescript
   const mnemonic = process.env.WALLET_MNEMONIC;
   ```

2. **Secret Management Services**: Use services like:
   - AWS Secrets Manager
   - HashiCorp Vault
   - Azure Key Vault
   - GitHub Secrets (for CI/CD environments)

3. **Encrypted Files**: If you must store mnemonics locally:
   - Use strong encryption (AES-256)
   - Store encryption keys separately
   - Keep the encrypted file outside your codebase

## Handling Private Keys

Private keys are the most sensitive component of your wallet. Follow these strict guidelines:

### Never Hardcode Private Keys
- **Never** embed private keys in your source code
- **Never** commit private keys to version control
- **Never** log or print private keys in development environments

### Secure Private Key Management
1. **Environment Variables**: Store private keys in environment variables
   ```typescript
   const privateKey = process.env.PRIVATE_KEY;
   ```

2. **Temporary Storage**: For production environments:
   - Use short-lived credentials
   - Implement proper key rotation
   - Use hardware security modules (HSMs) when possible

3. **Key Derivation**: For derived keys:
   - Use strong key derivation functions (like PBKDF2, Argon2)
   - Never use weak derivation methods
   - Always use appropriate iteration counts

## Best Practices for Agent Logic

### Input Validation
- Always validate all wallet-related inputs
- Never trust user-provided wallet addresses or public keys
- Implement proper error handling for invalid inputs

### Secure Transactions
- Never sign transactions with hardcoded keys
- Always verify transaction signatures
- Implement proper gas limit calculations
- Use transaction simulation before execution

### Logging and Monitoring
- Never log private keys or sensitive transaction data
- Implement proper logging levels (avoid logging sensitive information at debug level)
- Set up monitoring for suspicious wallet activities
- Use secure logging mechanisms that don't expose sensitive data

## Development Security Checklist

Before deploying any wallet-related functionality:

1. [ ] All mnemonics and private keys are stored securely (not in code)
2. [ ] Environment variables are properly secured (not committed to version control)
3. [ ] All sensitive data is properly encrypted at rest
4. [ ] Input validation is implemented for all wallet operations
5. [ ] No sensitive data is logged or exposed in error messages
6. [ ] Proper error handling prevents information leakage
7. [ ] All dependencies are up-to-date and secure
8. [ ] Code has been reviewed for security vulnerabilities

## Example: Secure Wallet Initialization

```typescript
// Secure wallet initialization example
function initializeWallet() {
  // Load from environment variables
  const mnemonic = process.env.WALLET_MNEMONIC;
  const privateKey = process.env.PRIVATE_KEY;

  if (!mnemonic || !privateKey) {
    throw new Error("Wallet credentials not properly configured");
  }

  // Validate credentials before use
  if (mnemonic.length < 12 || privateKey.length < 64) {
    throw new Error("Invalid wallet credentials");
  }

  // Initialize wallet with secure context
  const wallet = new Wallet({
    mnemonic,
    privateKey,
    network: process.env.NETWORK || "mainnet"
  });

  return wallet;
}
```

## Additional Resources

- [Fuel Wallet Documentation](https://docs.fuel.sh/)
- [Secure Coding Practices](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_Practices_Cheat_Sheet.html)
- [OWASP Wallet Security Guide](https://cheatsheetseries.owasp.org/cheatsheets/Wallet_Security_Cheat_Sheet.html)
