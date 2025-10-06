// test/test.js - Simple test file
const DiscardAPI = require('../dist/index.cjs');

const API_KEY = 'YOUR_API_KEY_HERE'; // Replace with your actual API key

async function runTests() {
  console.log('🧪 Starting Discard API SDK Tests...\n');

  const api = new DiscardAPI({ 
    apiKey: API_KEY,
    fullResponse: false // Test with result-only mode
  });

  const tests = [
    {
      name: 'URL Shortener',
      fn: () => api.shortenClck('https://github.com/GlobalTechInfo/GlobalTechInfo.git')
    },
    {
      name: 'Dad Joke',
      fn: () => api.dadJoke()
    },
    {
      name: 'Random Quote',
      fn: () => api.RandomQuote()
    },
    {
      name: 'Cat Image',
      fn: () => api.CatImage()
    },
    {
      name: 'Fake User',
      fn: () => api.FakeUser()
    },
    {
      name: 'QR Code',
      fn: () => api.QRCode('Hello World')
    },
    {
      name: 'Date Fact',
      fn: () => api.DateFact(7, 5)
    },
    {
      name: 'Base64 Encode',
      fn: () => api.base64Encode('Hello World')
    }
  ];

  let passed = 0;
  let failed = 0;

  for (const test of tests) {
    try {
      console.log(`▶️  Testing: ${test.name}...`);
      const result = await test.fn();
      console.log(`✅ ${test.name}: PASSED`);
      console.log(`   Result:`, JSON.stringify(result).substring(0, 100) + '...\n');
      passed++;
    } catch (error) {
      console.error(`❌ ${test.name}: FAILED`);
      console.error(`   Error: ${error.message}\n`);
      failed++;
    }
  }

  console.log('\n📊 Test Summary:');
  console.log(`   Total: ${tests.length}`);
  console.log(`   ✅ Passed: ${passed}`);
  console.log(`   ❌ Failed: ${failed}`);
  
  if (failed === 0) {
    console.log('\n🎉 All tests passed!');
  }

  // Test fullResponse mode
  console.log('\n🔄 Testing fullResponse mode...');
  api.setFullResponse(true);
  try {
    const result = await api.getRandomQuote();
    console.log('✅ Full response:', result);
    console.log(`   Has "status" field: ${!!result.status}`);
    console.log(`   Has "creator" field: ${!!result.creator}`);
    console.log(`   Has "result" field: ${!!result.result}`);
  } catch (error) {
    console.error('❌ Full response test failed:', error.message);
  }
}

// Only run if API_KEY is set
if (API_KEY === 'YOUR_API_KEY_HERE') {
  console.error('❌ Please set your API key in test.js before running tests!');
  process.exit(1);
}

runTests().catch(console.error);
